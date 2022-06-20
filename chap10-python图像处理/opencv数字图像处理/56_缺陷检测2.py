import cv2


def get_template(binary, boxes):
    x, y, w, h = boxes[0]
    roi = binary[y:y + h, x:x + w]
    return roi


def detect_defect(binary, boxes, tpl):
    height, width = tpl.shape
    index = 1
    defect_rois = []
    # 发现缺失
    for x, y, w, h in boxes:
        roi = binary[y:y + h, x:x + w]
        roi = cv2.resize(roi, (width, height))
        mask = cv2.subtract(tpl, roi)
        se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5), (-1, -1))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se)
        ret, mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)
        count = 0
        for row in range(height):
            for col in range(width):
                pv = mask[row, col]
                if pv == 255:
                    count += 1
        if count > 0:
            defect_rois.append([x, y, w, h])

        index += 1
    return defect_rois


src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 图像二值化
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3), (-1, -1))
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, se)
cv2.imshow("binary", binary)

# 轮廓提取
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
height, width = src.shape[:2]
rects = []
for c in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[c])
    area = cv2.contourArea(contours[c])
    if h > (height // 2):
        continue
    if area < 150:
        continue
    rects.append([x, y, w, h])

# 排序轮廓
rects = sorted(rects, key=lambda x: x[1])
print(rects)
template = get_template(binary, rects)

# 填充边缘
for c in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[c])
    area = cv2.contourArea(contours[c])
    if h > (height // 2):
        continue
    if area < 150:
        continue
    cv2.drawContours(binary, contours, c, (0), 2, 8)
cv2.imshow("template", template)

# 检测缺陷
defect_boxes = detect_defect(binary, rects, template)
for dx, dy, dw, dh in defect_boxes:
    cv2.rectangle(src, (dx, dy), (dx + dw, dy + dh), (0, 0, 255), 1, 8, 0)
    cv2.putText(src, "bad", (dx, dy - 2), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0), 2)

index = 1
for dx, dy, dw, dh in rects:
    cv2.putText(src, "num:%d" % index, (dx - 52, dy + 30), cv2.FONT_HERSHEY_SIMPLEX, .5, (30, 122, 233), 2)
    index += 1

cv2.imshow("result", src)


cv2.waitKey(0)
cv2.destroyAllWindows()

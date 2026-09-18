def box_to_slice(box):
    x, y, w, h = box
    return y, y + h, x, x + w

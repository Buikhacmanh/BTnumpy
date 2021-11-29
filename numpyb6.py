import numpy as np

arr = np.array([[7, 4, 2], [3, 9, 5]])
print("median arr (axis = 0) = ", np.median(arr, axis=0))
print("median arr (axis = 1) = ", np.median(arr, axis=1))
freetuts_visitors = np.array([3776, 3112, 3476, 3319, 3559, 2121, 3462])
print("Số người truy cập trung bình mỗi ngày trong tuần qua của Freetuts: ", np.mean(freetuts_visitors))

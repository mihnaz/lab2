import os
import cv2
from logger import Logger
from image_processing import unsharp_mask,gray_world_fast

UNSHARP_MASKING = "Повышение резкости (UnsharpMasking)."
WHITE_BALANCE = "Баланс белого: Метод «Серого мира»"

def check_readable(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл не найден: {path}")
    if not os.path.isfile(path):
        raise IsADirectoryError(f"Путь не является файлом: {path}")
    if not os.access(path, os.R_OK | os.W_OK):
        raise PermissionError(f"Нет прав на чтение файла: {path}")

def main():


    input_file = input("Введите файл для обработки: ")
    input_path = f"Lab2_Media/data/input/{input_file}"
    output_path = "Lab2_Media/data/output/result.jpg"
    logger = Logger("Lab2_Media/logs/history.txt")

    try:
        check_readable(input_path)
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        print(f"Ошибка чтения: {e}")
        logger.log(file=input_file, filter=UNSHARP_MASKING, is_correct=False)
        logger.log(file=input_file, filter=UNSHARP_MASKING, is_correct=False)
        return

    img = cv2.imread(input_path)
    if img is None:
        print(f"Ошибка: не удалось прочитать или декодировать файл {input_path}")
        logger.log(file=input_file, filter=UNSHARP_MASKING, is_correct=False)
        logger.log(file=input_file, filter=UNSHARP_MASKING, is_correct=False)
        return


    result1 = unsharp_mask(img)
    logger.log(file=input_file,filter=UNSHARP_MASKING,is_correct=True)
    result2 = gray_world_fast(result1)
    logger.log(file=input_file,filter=WHITE_BALANCE,is_correct=True)

    ok = cv2.imwrite(output_path, result2)
    if not ok:
        print(f"Ошибка: cv2.imwrite не смог записать файл {output_path}")
        return



if __name__ == "__main__":
    main()
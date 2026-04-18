import numpy as np

def main():
    try:
        x = input("x 값:").strip()
        y = input("y 값:").strip() 

        x_val = float(x)
        y_val = float(y)

        result = np.power(x_val, y_val)
        print(f"{x_val} ** {y_val} = {result}")

    except ValueError:
        print("제대로 하자")
    except Exception as e:
        print("오류:", e)

# def main():
#     try:
#         x = input("x 값을 입력하세요: ").strip()
#         y = input("y 값을 입력하세요: ").strip()
#         x_val = float(x)
#         y_val = float(y)
#         result = np.power(x_val, y_val)
#         print(f"{x_val} ** {y_val} = {result}")
#     except ValueError:
#         print("숫자를 올바르게 입력해주세요.")
#     except Exception as e:
#         print("오류:", e)

if __name__ == "__main__":
    main()

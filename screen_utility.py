import pyautogui

class ScreenUtility:
    def __init__(self):
        pass

    def click_at_position(self, x, y):
        # 指定された位置に移動してクリック
        pyautogui.moveTo(x, y)
        pyautogui.click()

    def take_screenshot(self, file_path):
        # スクリーンショットを撮影
        screenshot = pyautogui.screenshot()
        # 指定されたファイルパスに保存
        screenshot.save(file_path)

    def find_image_position(self, image_path):
        # 画面上で指定された画像を検索
        location = pyautogui.locateOnScreen(image_path)
        if location is not None:
            # 画像の中心座標を取得
            center = pyautogui.center(location)
            return center
        else:
            return None

# 使用例
utility = ScreenUtility()
utility.click_at_position(100, 200)
utility.take_screenshot("screenshot.png")
position = utility.find_image_position("target_image.png")
if position:
    print(f"画像の位置: {position}")
else:
    print("画像が見つかりませんでした")
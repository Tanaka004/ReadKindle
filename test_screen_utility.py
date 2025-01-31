import unittest
from screen_utility import ScreenUtility
from unittest.mock import patch

class TestScreenUtility(unittest.TestCase):
    
    @patch('pyautogui.moveTo')
    @patch('pyautogui.click')
    def test_click_at_position(self, mock_click, mock_moveTo):
        utility = ScreenUtility()
        utility.click_at_position(100, 200)
        mock_moveTo.assert_called_once_with(100, 200)
        mock_click.assert_called_once()

    @patch('pyautogui.screenshot')
    def test_take_screenshot(self, mock_screenshot):
        mock_screenshot.return_value.save = unittest.mock.Mock()
        utility = ScreenUtility()
        utility.take_screenshot('test.png')
        mock_screenshot.assert_called_once()
        mock_screenshot.return_value.save.assert_called_once_with('test.png')

    @patch('pyautogui.locateOnScreen')
    @patch('pyautogui.center')
    def test_find_image_position(self, mock_center, mock_locateOnScreen):
        mock_locateOnScreen.return_value = (0, 0, 10, 10)
        mock_center.return_value = (5, 5)
        utility = ScreenUtility()
        position = utility.find_image_position('test_image.png')
        self.assertEqual(position, (5, 5))
        mock_locateOnScreen.assert_called_once_with('test_image.png')
        mock_center.assert_called_once_with((0, 0, 10, 10))

if __name__ == '__main__':
    unittest.main()
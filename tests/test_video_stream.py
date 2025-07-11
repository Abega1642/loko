import unittest
from unittest.mock import MagicMock, patch

from src.utils.video_stream import VideoStream


class TestVideoStream(unittest.TestCase):

    @patch("cv2.VideoCapture")
    def test_camera_initialization_default_index(self, mock_capture):
        vs = VideoStream()
        self.assertIsNotNone(vs.cap)

    @patch("cv2.VideoCapture")
    def test_camera_initialization_custom_index(self, mock_capture):
        VideoStream(index=2)
        mock_capture.assert_called_with(2)

    @patch("cv2.VideoCapture")
    def test_read_successful(self, mock_capture):
        mock_instance = MagicMock()
        mock_instance.read.return_value = (True, "mock_frame")
        mock_capture.return_value = mock_instance
        vs = VideoStream()
        frame = vs.read()
        self.assertEqual(frame, "mock_frame")

    @patch("cv2.VideoCapture")
    def test_read_failure(self, mock_capture):
        mock_instance = MagicMock()
        mock_instance.read.return_value = (False, None)
        mock_capture.return_value = mock_instance
        vs = VideoStream()
        with self.assertRaises(RuntimeError):
            vs.read()

    @patch("cv2.VideoCapture")
    def test_release_method_calls_capture_release(self, mock_capture):
        mock_instance = MagicMock()
        mock_capture.return_value = mock_instance
        vs = VideoStream()
        vs.release()
        mock_instance.release.assert_called_once()

    @patch("cv2.VideoCapture")
    def test_multiple_reads(self, mock_capture):
        mock_instance = MagicMock()
        mock_instance.read.side_effect = [(True, "frame1"), (True, "frame2")]
        mock_capture.return_value = mock_instance
        vs = VideoStream()
        self.assertEqual(vs.read(), "frame1")
        self.assertEqual(vs.read(), "frame2")

    @patch("cv2.VideoCapture")
    def test_stream_is_opened_on_init(self, mock_capture):
        mock_instance = MagicMock()
        mock_instance.isOpened.return_value = True
        mock_capture.return_value = mock_instance
        vs = VideoStream()
        self.assertTrue(vs.cap.isOpened())

    @patch("cv2.VideoCapture")
    def test_stream_closed(self, mock_capture):
        mock_instance = MagicMock()
        mock_instance.isOpened.return_value = False
        mock_capture.return_value = mock_instance
        vs = VideoStream()
        self.assertFalse(vs.cap.isOpened())

    @patch("cv2.VideoCapture")
    def test_read_returns_non_none_frame(self, mock_capture):
        mock_instance = MagicMock()
        mock_instance.read.return_value = (True, "img")
        mock_capture.return_value = mock_instance
        vs = VideoStream()
        self.assertIsNotNone(vs.read())

    @patch("cv2.VideoCapture")
    def test_release_does_not_throw_error(self, mock_capture):
        mock_instance = MagicMock()
        mock_capture.return_value = mock_instance
        vs = VideoStream()
        try:
            vs.release()
        except Exception as e:
            self.fail(f"release raised unexpected exception: {e}")

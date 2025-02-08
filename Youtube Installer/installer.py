import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from gui import Ui_MainWindow
from yt_dlp import YoutubeDL

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.download)

    def download(self):
        link = self.lineEdit.text()
        if not link:
            QMessageBox.warning(self, "Error", "Please enter a valid URL")
            return

        downloads_path = str(Path.home() / "Downloads")
        
        try:
            ydl_opts = {
                'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
                'keepvideo': True,
                'audio_codec': 'mp4',
                'ffmpeg_location': "C:/Users/S H K/Downloads/ffmpeg-2025-01-05-git-19c95ecbff-full_build/ffmpeg-2025-01-05-git-19c95ecbff-full_build/bin",
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
            }],
}

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            
            QMessageBox.information(self, "Success", f"Video downloaded successfully to {downloads_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
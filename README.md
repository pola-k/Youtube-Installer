# YouTube Installer

A Python-based application with a Qt-designed GUI that facilitates downloading videos from YouTube using the `youtube-dl` library.

## Features

- Download videos from YouTube.
- User-friendly graphical interface designed with Qt Designer.
- Supports various video formats and resolutions.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**: Download and install the latest version from the [official Python website](https://www.python.org/).
- **youtube-dl**: Install via pip:

  ```bash
  pip install youtube-dl
  ```

  For more information, refer to the [youtube-dl documentation](https://youtube-dl.readthedocs.io/).

- **PyQt5**: Install via pip:

  ```bash
  pip install PyQt5
  ```

## Installation

**Clone the Repository**:

   ```bash
   git clone https://github.com/pola-k/Youtube-Installer.git
   cd Youtube-Installer
   ```
      
## Usage

1. **Run the Application**:

   ```bash
   python installer.py
   ```

2. **Using the GUI**:

   - Enter the URL of the YouTube video you wish to download.
   - Click the 'Download' button to start the process.

## Acknowledgements

- [youtube-dl](https://github.com/ytdl-org/youtube-dl) for the powerful video downloading library.
- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) for the GUI framework.

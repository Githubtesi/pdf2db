Anacondaを使用
https://anaconda.org/channels/conda-forge/packages/conda/files
conda 25.5.1 をインストール


1. 外部ツールのインストール
① Tesseract OCR (文字認識エンジン)
画像から文字を読み取るための本体。

配布元: UB-Mannheim/tesseract

手順: tesseract-ocr-w64-setup-v5.x.x...exe をダウンロードして実行。
tesseract-ocr-w64-setup-5.5.0.20241111.exe　を使用

注意: インストール途中の「Additional language data」で 「Japanese」 と 「Japanese (vertical)」 に必ずチェックを入れてください。

② Poppler for Windows (PDF変換ツール)
PDFを画像に変換するために必要。
配布元: Oshani/poppler-windows (または github.com/oschani/poppler-windows)
poppler-23.11.0　を使用

手順:
1.  .zip ファイルをダウンロードして解凍。
2.  解凍したフォルダを C:\ 直下に置き、名前を poppler-23.11.0 に変更してください（コード内の POPLER_PATH と一致させるため）。
3.  C:\poppler-23.11.0\Library\bin という階層があることを確認してください。

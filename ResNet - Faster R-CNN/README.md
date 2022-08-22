Über dieses Notebook lässt sich ein ResNet50-Faster-R-CNN-Modell trainieren. Das Notebook beruht auf "https://www.kaggle.com/code/scratchpad/notebook550dad3591/edit" und wurde leicht abgeändert.

Der Datensatz muss im COCO-Format bereitgestellt werden. Die Verzeichnisstruktur sollte wie folgt aussehen:
  - path/to/data
      - train
          - coco_annotations.json
          - img1.jpg
          - img2.jpg
          - ...
      - test
          - coco_annotations.json
          - img3.jpg
          - img4.jpg
          - ...

Die Pfade müssen entsprechend im Notebook hinterlegt werden.

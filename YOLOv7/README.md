Über das Notebook lässt sich YOLOv7 mit einem eigenen Datensatz trainieren. 

Notwendige Schritte:
  - Erstellen der Datein "custom.yaml" unter /yolov7/data
  - Hochladen der Bilder und Labels unter /yolov7/data/images und /yolov7/data/labels
  - Anpassen der custom.yaml datei:
      -   train: path/to/yolov7/data/images/train # train images
          val: path/to/yolov7/data/images/test # val images
          # Classes
          nc: x  # number of classes
          names: ['klasse1', 'klasse2', 'klasse3']  # class names
  - Die Verzeichnisstruktur sollte so aussehen:
        - data
            - images
                - train
                    - img1.jpg
                    - ...
                - test
            - labels
                - train
                    - img1.txt
                - test

  - Die ".txt"-Dateien der Label sind wie folgt aufgebaut:
      - klasse_id x_center y_center width height
      - ...
  - Dabei sind die koordinaten auf die Bildgräße relativiert

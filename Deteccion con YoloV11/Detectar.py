from ultralytics import YOLO

model = YOLO("bestModeloEntrenadoEnCasa.pt")

results = model("gastrotrico.mp4",show=True,save=True)
for result in results:
    xywh = result.boxes.xywh  # centros
    xywhn = result.boxes.xywhn  # centros normalizados
    xyxy = result.boxes.xyxy  # top-left-x, top-left-y, bottom-right-x, bottom-right-y
    xyxyn = result.boxes.xyxyn  # normalized
    names = [result.names[cls.item()] for cls in result.boxes.cls.int()]  # nombre de la clase
    confs = result.boxes.conf  # confidence score of each box
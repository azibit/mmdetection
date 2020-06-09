from .coco import CocoDataset
from .builder import DATASETS
from .xml_style import XMLDataset
from .voc import VOCDataset
@DATASETS.register_module
class MyDataset(XMLDataset):

    CLASSES = ('ear')

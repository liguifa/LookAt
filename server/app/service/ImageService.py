from ..domain import Image
from .baseService import BaseService


class ImageService(BaseService):
    def __init__(self):
        super().__init__()

    def get_images(self, page_index, page_size, order_by, is_asc):
        return Image.query.order_by(Image.id)
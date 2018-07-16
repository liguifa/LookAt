class Image:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.thumbnail = ""
        self.url = ""
        self.upload_time = ""
        self.upload_user = ""

    @classmethod
    def convert_to_images(cls, entity_images):
        images = []
        for entity_image in entity_images:
            image = Image()
            image.id = entity_image.id
            image.name = entity_image.name
            image.url = entity_image.url
            image.upload_time = entity_image.upload_time
            image.upload_user = entity_image.upload_user
            image.thumbnail = "/api/images/thumbnail{image.id}".format(**locals())  # NOQA
            images.append(image)
        return images

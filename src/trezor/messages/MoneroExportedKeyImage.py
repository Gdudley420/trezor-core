# Automatically generated by pb2py
# fmt: off
import protobuf as p


class MoneroExportedKeyImage(p.MessageType):

    def __init__(
        self,
        iv: bytes = None,
        blob: bytes = None,
    ) -> None:
        self.iv = iv
        self.blob = blob

    @classmethod
    def get_fields(cls):
        return {
            1: ('iv', p.BytesType, 0),
            3: ('blob', p.BytesType, 0),
        }

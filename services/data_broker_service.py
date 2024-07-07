import typing as t
import bentoml
from common.utils import get_data_head


@bentoml.service()
class DataBrokerService:
    def __init__(self):
        self.data_head = get_data_head()

    @bentoml.api()
    def get_data_head(self) -> t.List[t.Dict[str, t.Any]]:
        return self.data_head.to_dict(orient='records')

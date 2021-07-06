import pytorch_lightning as pl


class PythonPipTestModel(pl.LightningModule):
    def __init__(self):
        super().__init__()
        pass

    def forward(self, *args, **kwargs) -> Any:
        pass

    def training_step(self, *args, **kwargs) -> STEP_OUTPUT:
        pass

    def validation_step(self, *args, **kwargs) -> Optional[STEP_OUTPUT]:
        pass

    def test_step(self, *args, **kwargs) -> Optional[STEP_OUTPUT]:
        pass

    def configure_optimizers(self):
        pass

    def prepare_data(self) -> None:
        pass

    def train_dataloader(self) -> Union[DataLoader, List[DataLoader], Dict[str, DataLoader]]:
        pass

    def val_dataloader(self) -> Union[DataLoader, List[DataLoader]]:
        pass

    def test_dataloader(self) -> Union[DataLoader, List[DataLoader]]:
        pass

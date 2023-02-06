import torch
import modules.safe as safe
import webui

torch.load = safe.unsafe_torch_load
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

def noop(*args, **kwargs):
    pass

def register_model():
    global model
    try:
        from modules import shared, sd_hijack
        shared.sd_model = model
        sd_hijack.model_hijack.hijack(model)
    except:
        print("Failed to hijack model.")

def init():
    global model
    import modules.sd_models
    modules.sd_models.list_models()
    modules.sd_models.list_models = noop
    model = modules.sd_models.load_model()
    modules.sd_models.load_model = noop
    register_model()

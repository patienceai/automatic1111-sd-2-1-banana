import torch
import modules.safe as safe
import webui

torch.load = safe.unsafe_torch_load
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

list_models = None
load_model = None

def noop(*args, **kwargs):
    pass

def unload_model():
    from modules import shared, sd_hijack, devices
    import gc
    if shared.sd_model:
         sd_hijack.model_hijack.undo_hijack(shared.sd_model)
         shared.sd_model = None
         gc.collect()
         devices.torch_gc()

def register_model():
    global model
    try:
        from modules import shared, sd_hijack
        if shared.sd_model is not model:
            unload_model()
            shared.sd_model = model
            sd_hijack.model_hijack.hijack(model)
            print("Loaded default model.")
    except:
        print("Failed to hijack model.")


def load_model_by_url(url):
    global list_models, load_model
    import modules.sd_models
    import hashlib
    hash_object = hashlib.md5(url.encode())
    md5_hash = hash_object.hexdigest()

    from download_checkpoint import download
    download(url, md5_hash)

    modules.sd_models.list_models = list_models
    modules.sd_models.load_model = load_model

    modules.sd_models.list_models()

    for m in modules.sd_models.checkpoints_list.values():
        if md5_hash in m.name:
            load_model(m)
            break

    modules.sd_models.list_models = noop
    modules.sd_models.load_model = noop

def init():
    global model, list_models, load_model
    import modules.sd_models

    modules.sd_models.list_models()

    list_models = modules.sd_models.list_models
    modules.sd_models.list_models = noop

    model = modules.sd_models.load_model()

    load_model = modules.sd_models.load_model
    modules.sd_models.load_model = noop

    register_model()

# 🍌 Stable Diffusion WebUI for banana (Stable Diffusion 1.5)

Deploy an API for AUTOMATIC1111's [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) to generate images with **Stable Diffusion 1.5**. Access txt2img, img2img and interrogation in one deployment!

Supports features not available in other Stable Diffusion templates, such as:

* [Prompt emphasis](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#attentionemphasis)
* [Prompt editing](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#prompt-editing)
* [Unlimited prompt length](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#infinite-prompt-length)

This deployment provides an API only and does not include the WebUI's user interface. Please report any issues you encounter.

## Instant Deploy

[See how to deploy in seconds](https://app.banana.dev/templates/patienceai/stable-diffusion-1.5-automatic1111).

## Model Inputs

### txt2img example

```
{
  "endpoint": "txt2img",
  "params": {
    "prompt": "an astronaut riding a (horse:motorcycle:0.5) on the moon",
    "negative_prompt": "cartoonish, low quality",
    "steps": 25,
    "sampler_name": "Euler a",
    "cfg_scale": 7.5,
    "seed": 42,
    "batch_size": 1,
    "n_iter": 1,
    "width": 512,
    "height": 512,
    "tiling": false
    
  }
}
```

(Only `prompt` is required.)

Output:

```
{
  "images": [
    "<base64 image>"
  ]
}
```

### img2img example

```
{
  "endpoint": "img2img",
  "params": {
    "prompt": "an astronaut riding a horse on the moon in anime style",
    "negative_prompt": "cartoonish, low quality",
    "steps": 25,
    "sampler_name": "Euler a",
    "cfg_scale": 7.5,
    "denoising_strength": 0.7,
    "seed": 42,
    "batch_size": 1,
    "n_iter": 1,
    "width": 512,
    "height": 512,
    "tiling": false
    "init_images": [
        "<base64 image>"
    ]
  }
}
```

(Only `prompt` and `init_images` are required.)

Output:

```
{
  "images": [
    "<base64 image>"
  ]
}
```

### Interrogation example

Interrogation takes an input image and generates a Stable Diffusion prompt that can be used to generate similar images.

```
{
  "endpoint": "interrogate",
  "params": {
    "image": "<base64 image>"
  }
}
```

Output:

```
{
  "caption": "<interrogate result>"
}
```

### Other endpoints

Other AUTOMATIC1111 API endpoints are not officially supported yet and may or may not work. Several download additional models at runtime. Please report any issues you encounter.

For full documentation of available endpoints and their parameters, run a local copy of the Stable Diffusion WebUI and visit http://localhost:7860/docs.

Model inputs should be in the following format:

```
{
  "endpoint": "<endpoint>",
  "params": {
    ...
  }
}
```

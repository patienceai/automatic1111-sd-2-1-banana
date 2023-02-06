
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

### Compatibility with other Banana 1-click deployments

For txt2img generation of a single image, you can use the same input format as other Banana deployments:

```
{
  "prompt": "an astronaut riding a (horse:motorcycle:0.5) on the moon",
  "negative_prompt": "cartoonish, low quality",
  "num_inference_steps": 25,
  "guidance_scale": 7.5,
  "seed": 42,
  "width": 512,
  "height": 512
}
```

(Only `prompt` is required.)

Output:

```
{
  "image_base64": "<BASE64_STRING>"
}
```

### Advanced txt2img example

For more control and direct access to the AUTOMATIC1111 API, use this alternative format:

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
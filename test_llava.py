from llava.mm_utils import get_model_name_from_path
from llava.eval.run_llava import eval_model


def run_llava(prompt, image_file, model_path='liuhaotian/llava-v1.5-7b'):    
    args = type('Args', (), {
        "model_path": model_path,
        "model_base": None,
        "model_name": get_model_name_from_path(model_path),
        "query": prompt,
        "conv_mode": None,
        "image_file": image_file,
        "sep": ",",
        "temperature": 0,
        "top_p": None,
        "num_beams": 1,
        "max_new_tokens": 512
    })()
    return eval_model(args) 


if __name__ == '__main__':
    prompt = 'What are the things I should be cautious about when I visit here?'
    image_file = 'https://llava-vl.github.io/static/images/view.jpg'
    res = run_llava(prompt, image_file)
    print('\nResult 1:\n', res)

    prompt = 'What do you see on this picture?'
    image_file = 'https://i.natgeofe.com/n/cad5d203-d715-4392-881c-3f33312652fe/00000169-ca0e-dfb8-a969-ea4e727d0002_3x2.jpg?wp=1&w=1436&h=958'
    res = run_llava(prompt, image_file)
    print('\nResult 2:\n', res)
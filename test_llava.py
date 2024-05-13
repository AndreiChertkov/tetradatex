from llava.eval.run_llava import eval_model


def test_llava(model_path='liuhaotian/llava-v1.5-7b'):
    prompt = 'What are the things I should be cautious about when I visit here?'
    image_file = 'https://llava-vl.github.io/static/images/view.jpg'
    
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
    res = eval_model(args) 
    
    print(res)


if __name__ == '__main__':
    test_llava()
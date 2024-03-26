import gradio as gr
import audio2face as a2f
import settings as st
import tempfile


def UploadAudio(audio:str):
    audio_fullname=audio.split("\\")[-1]
    audio_name,audio_format=audio_fullname.split('.')
    audio_directory=audio.replace(audio_fullname,'')
    if audio_format != 'wav':
        print("Error")
    return audio_directory,audio_fullname
def UploadModel(model:str):
    if model=="Custom":
        pass
    return st.MODEL_CHOICE.get(model)

def main_process(audios,model_choice,
                 export_dir,
                 fps,
                 export_format=st.DEFAULT_SETTINGS["ExportFormat"]):
    res=""
    for audio in audios:
            
        audio_dir,audio_name=UploadAudio(audio.name)
        model_url=UploadModel(model_choice)
        
        res+=a2f.Audio2face(model=model_url,
                            audio_directory=audio_dir,
                            audio_name=audio_name,
                            FPS=fps,
                            export_format=export_format,
                            export_path=export_dir)
    
    return res
    
    

input_audios=gr.File(file_count="multiple",type="file",file_types=["audio"])
model_dropdown_button=gr.Dropdown(choices=st.MODEL_CHOICE.keys(),label="Choose Model",info="选择一个面部模型")
export_dir=gr.Textbox(label="选择导出路径",info="默认为工作目录下的export文件夹",value=st.DEFAULT_SETTINGS["ExportDirectory"])
fps_input=gr.Number(label="设置导出FPS",minimum=0,maximum=120,step=1,value=60)


app=gr.Interface(
    fn=main_process,
    inputs=[input_audios,model_dropdown_button,export_dir,fps_input],
    outputs=gr.Text()
)

app.launch(share=True,inbrowser=True)
import requests
import settings as st
from typing import Literal
url="http://localhost:8011"



def load_usd(model):
    
    
    req_body={
        
        "file_name":model
    }
    
    
    res = requests.post(st.LOAD_MODEL_API["Load"],json=req_body).json()
    
    
    return f"response of load model {model} : {res}\n"
    
def get_instance()->str:
    res = requests.get(st.GET_INSTANCE_API["GetInstance"]).json()
    return res.get('result').get('regular')[0]

def load_audio(player_name,audio_name,audio_path):

    
    dict1={
        "a2f_player": player_name,
        "dir_path": audio_path
    }
    dict2={
        "a2f_player": player_name,
        "file_name": audio_name
    }
    
    res1=requests.post(st.LOAD_AUDIO_API["SetTrackDirectory"],json=dict1).json()
    res2=requests.post(st.LOAD_AUDIO_API["SetTrack"],json=dict2).json()
    
    
    return f"response of setting sound dir to {audio_path}: {res1}\n"+f"response of upload sound {audio_name} : {res2}\n"
    
def export_blendshape(export_path,export_name,export_format:Literal["json","usd"]="json",fps=60,isBatch=False):
    
    def get_solver_node()->str:
        
        res=requests.get(st.GET_SOLVER_API["GetBSSolver"]).json()
        return res.get('result')[0]
    
    solver_node = get_solver_node()
    
    param={
        "solver_node": solver_node,
        "export_directory": export_path,
        "file_name": export_name,
        "format": export_format,
        "batch": isBatch,
        "fps": fps
    }    
    api="A2F/Exporter/ExportBlendshapes"
    res=requests.post(st.EXPORT_BLENDSHAPE_API["ExportBS"],json=param).json()
    
    if res.get('status')=='OK':
        return f"Successfully export {export_name} to {export_path} as {export_format}!"
    
    return f"response of export BS to {export_path} as {export_format} : {res}\n"
    
def Audio2face(model,audio_directory,audio_name,FPS,export_format,export_path):
    
    res1=load_usd(model)
    
    res2=load_audio(get_instance(),audio_name,audio_directory)
    
    res3=export_blendshape(export_path,f"{audio_name}",export_format,FPS)    

    return res1+res2+res3
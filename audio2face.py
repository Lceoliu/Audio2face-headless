import os,requests

url="http://localhost:8011"

usd_path=os.path.abspath('.')+"\\usd"
audio_path=os.path.abspath('.')+"\\audios"
export_path=os.path.abspath('.')+"\\export"

audio_name="hello.wav"

def load_usd(usd_name):
    api="/A2F/USD/Load"
    
    req_body={
        # "file_name":usd_path+'/'+usd_name
        "file_name":"omniverse://localhost/NVIDIA/Assets/Audio2Face/Samples_2023.1/blendshape_solve/claire_solved_arkit.usd"
    }
    res = requests.post(url+api,json=req_body).json()
    print(res)
def get_instance()->str:
    api = "/A2F/Player/GetInstances"
    res = requests.get(url+api).json()
    return res.get('result').get('regular')[0]
def load_audio(player_name,audio_name):
    api1="/A2F/Player/SetRootPath"
    api2="/A2F/Player/SetTrack"
    
    dict1={
        "a2f_player": player_name,
        "dir_path": audio_path
    }
    dict2={
        "a2f_player": player_name,
        "file_name": audio_name
    }
    res1=requests.post(url+api1,json=dict1).json()
    res2=requests.post(url+api2,json=dict2).json()
    print(res1,res2)
    
def export_blendshape(export_name,fps):
    
    def get_solver_node()->str:
        api="/A2F/Exporter/GetBlendShapeSolvers"
        res=requests.get(url+api).json()
        return res.get('result')[0]
    
    solver_node = get_solver_node()
    
    param={
        "solver_node": solver_node,
        "export_directory": export_path,
        "file_name": export_name,
        "format": "json",
        "batch": False,
        "fps": fps
    }    
    api="A2F/Exporter/ExportBlendshapes"
    res=requests.post(url+'/'+api,json=param).json()
    print(res)
    
if __name__=="__main__":
    load_usd('claire_solved_arkit.usd')
    instance_name=get_instance()
    load_audio(instance_name,audio_name)
    
    export_blendshape(f"export blendshape {audio_name}",30)
    
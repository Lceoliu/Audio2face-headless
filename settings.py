import os
# Audio2Face默认服务器端口
BASE_URL="http://localhost:8011"

CURRENT_ABSPATH=os.path.abspath(".")
# default solved face usd
# PS:要使用默认模型,必须保证omniverse的nucleus服务器处于启动状态
# PPS:以下默认路径基于Audio2Face Ver 2023.1.1,不保证其他版本下路径是否会改变
CLAIRE_FACE_URL="omniverse://localhost/NVIDIA/Assets/Audio2Face/Samples_2023.1/blendshape_solve/claire_solved_arkit.usd"

MODEL_CHOICE={
    "Claire":CLAIRE_FACE_URL,
    
}




# 加载音频文件的api
# 音频文件必须是.wav格式!!!
LOAD_AUDIO_API={
    "SetTrackDirectory":BASE_URL+"/A2F/Player/SetRootPath",
    "SetTrack":BASE_URL+"/A2F/Player/SetTrack"
}

# 加载面部模型的api
# 面部模型必须是.usd格式,且带有blendshape数据
LOAD_MODEL_API={
    "Load":BASE_URL+"/A2F/USD/Load"
}

GET_INSTANCE_API={
    "GetInstance":BASE_URL+"/A2F/Player/GetInstances"
}

GET_SOLVER_API={
    # 获取场景中的Blendshape Solver的路径
    "GetBSSolver":BASE_URL+"/A2F/Exporter/GetBlendShapeSolvers"
}

EXPORT_BLENDSHAPE_API={
    "ExportBS":BASE_URL+"/A2F/Exporter/ExportBlendshapes"
}

DEFAULT_SETTINGS={
    "AudioDirectory":"",
    "ExportDirectory":CURRENT_ABSPATH+"\\export",
    "ExportFPS":60,
    "ExportFormat":"json",
    
}

CUSTOM_SETTINGS={
    
}
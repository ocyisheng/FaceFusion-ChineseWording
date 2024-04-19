#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Any, Dict

CHINESE_WORDING_24: Dict[str, Any] = \
	{
		"python_not_supported": "Python版本不支持，更新 {version} 或更高版本",
		"ffmpeg_not_installed": "FFMpeg没有安装",
		"creating_temp": "创建临时资源",
		"extracting_frames": "提取分辨率为 {resolution} 和 {fps}/秒的帧",
		"extracting_frames_succeed": "提取帧成功",
		"extracting_frames_failed": "提取帧失败",
		"analysing": "分析中...",
		"processing": "处理中...",
		"downloading": "下载中...",
		"temp_frames_not_found": "未找到临时帧",
		"copying_image": "复制分辨率为 {resolution} 的图像",
		"copying_image_succeed": "复制图像成功",
		"copying_image_failed": "复制图像失败",
		"finalizing_image": "使用 {resolution} 的分辨率定稿图像",
		"finalizing_image_succeed": "定稿图像成功",
		"finalizing_image_skipped": "跳过定稿图像",
		"merging_video": "使用分辨率 {resolution} 和 {fps} 帧率合并视频",
		"merging_video_succeed": "合并视频成功",
		"merging_video_failed": "合并视频失败",
		"skipping_audio": "跳过音频",
		"restoring_audio_succeed": "还原音频成功",
		"restoring_audio_skipped": "已跳过还原音频 ",
		"clearing_temp": "清除临时资源",
		"processing_stopped": "处理已停止",
		"processing_image_succeed": "图像处理在 {seconds} 秒内成功",
		"processing_image_failed": "图像处理失败",
		"processing_video_succeed": "视频处理在 {seconds} 秒内成功",
		"processing_video_failed": "视频处理失败",
		"model_download_not_done": "模型的下载尚未完成",
		"model_file_not_present": "模型的文件不存在",
		"select_image_source": "选择源图像的路径 ",
		"select_audio_source": "为源路径选择音频 ",
		"select_video_target": "为目标路径选择视频频 ",
		"select_image_or_video_target": "选择目标图像或视频的路径",
		"select_file_or_directory_output": "选择输出路径的文件或目录 ",
		"no_source_face_detected": "未检测到源图像的脸部 ",
		"frame_processor_not_loaded": "无法加载帧处理器 {frame_proccessor}",
		"frame_processor_not_implemented": "帧处理器 {frame_proccessor}未正确实现",
		"ui_layout_not_loaded": "无法加载视图布局 {ui_layout}",
		"ui_layout_not_implemented": "视图布局 {ui_layout}未正确实现",
		"stream_not_loaded": "无法加载流 {stream_mode}",
		"point": ".",
		"comma": ",",
		"colon": ":",
		"question_mark": "?",
		"exclamation_mark": "!",
		"help": {
			"install_dependency": "选择要安装的依赖项 {dependency} 的变体",
			"skip_venv": "跳过虚拟环境检查",
			"source": "选择源图片",
			"target": "选择目标图片或视频",
			"output": "指定输出文件或目录",
			"skip_download": "忽略自动下载和查找",
			"headless": "在无头模式下运行程序 ",
			"log_level": "从可用日志等级中进行选择",
			"execution_providers": "从可用的执行程序中进行选择  (选项: {choices}, ...)",
			"execution_thread_count": "指定执行线程的数量 ",
			"execution_queue_count": "指定执行队列的数量 ",
			"video_memory_strategy": "指定处理视频内存的策略",
			"system_memory_limit": "指定要使用的系统内存量（GB）",
			"face_analyser_order": "指定用于脸部分析器的顺序",
			"face_analyser_age": "指定用于脸部分析器的年龄",
			"face_analyser_gender": "指定用于脸部分析器的性别",
			"face_detector_model": "指定用于脸部检测器的模型",
			"face_detector_size": "指定用于脸部检测器的大小阈值",
			"face_detector_score": "指定用于脸部检测器的分数阈值",
			"face_landmarker_score": "根据置信度评分筛选检测到的坐标",
			"face_selector_mode": "指定脸部选择器的模式",
			"reference_face_position": "指定参照脸的位置",
			"reference_face_distance": "指定参照脸和目标脸之间的相似度",
			"reference_frame_number": "指定参照帧的编号 ",
			"face_mask_types": "从可用的遮罩类型中进行选择  (选项: {choices})",
			"face_mask_blur": "指定遮罩的模糊量",
			"face_mask_padding": "指定遮罩填充（上、右、下、左）的百分比",
			"face_mask_regions": "从可用的口罩区域中进行选择  (选项: {choices})",
			"trim_frame_start": "指定提取的起始帧",
			"trim_frame_end": "指定提取的结束帧",
			"temp_frame_format": "指定用于帧提取的图像格式",
			"keep_temp": "处理后保留临时帧 ",
			"output_image_quality": "指定用于输出图像的质量 ",
			"output_image_resolution": "根据目标图像指定图像的输出分辨率",
			"output_video_encoder": "指定用于输出视频的编码器",
			"output_video_preset": "指定用于输出视频的预设 ",
			"output_video_quality": "指定用于输出视频的质量 ",
			"output_video_resolution": "指定用于输出视频的分辨率 ",
			"output_video_fps": "指定用于输出视频的每秒帧数（fps） ",
			"skip_audio": "省略目标的音频",
			"frame_processors": "从可用的帧处理器中进行选择 (选项: {choices}, ...)",
			"face_debugger_items": "指定脸部调试器的选择项 (选项: {choices})",
			"face_enhancer_model": "选择负责脸部增强的模型 ",
			"face_enhancer_blend": "混合已增强部分到上一个脸中",
			"face_swapper_model": "选择负责脸部替换的模型",
			"frame_enhancer_model": "选择负责帧增强的模型",
			"frame_enhancer_blend": "混合已增强部分到上一帧中",
			"lip_syncer_model": "选择负责嘴唇同步的模型",
			"ui_layouts": "从可用视图布局中进行选择 (选项: {choices}, ...)"
		},
		"uis": {
			"start_button": "开始",
			"stop_button": "结束",
			"clear_button": "清除",
			"donate_button": "捐赠",
			"benchmark_results_dataframe": "基准结果",
			"benchmark_runs_checkbox_group": "基准运行",
			"benchmark_cycles_slider": "基准周期",
			"common_options_checkbox_group": "选项",
			"execution_providers_checkbox_group": "执行提供者",
			"execution_queue_count_slider": "执行队列数",
			"execution_thread_count_slider": "执行线程数",
			"face_analyser_order_dropdown": "顺序脸部分析器",
			"face_analyser_age_dropdown": "年龄脸部分析器",
			"face_analyser_gender_dropdown": "性别脸部分析器",
			"face_detector_model_dropdown": "脸部检测器模型",
			"face_detector_size_dropdown": "脸部检测器大小",
			"face_detector_score_slider": "脸部检测器打分",
			"face_landmarker_score_slider": "面部坐标打分",
			"face_mask_types_checkbox_group": "遮罩类型",
			"face_mask_blur_slider": "遮罩模糊量",
			"face_mask_padding_top_slider": "遮罩填充上部",
			"face_mask_padding_right_slider": "遮罩填充右部",
			"face_mask_padding_bottom_slider": "遮罩填充下部",
			"face_mask_padding_left_slider": "遮罩填充左部",
			"face_mask_region_checkbox_group": "遮罩区域",
			"face_selector_mode_dropdown": "脸部选择器模式",
			"reference_face_gallery": "参考脸部",
			"reference_face_distance_slider": "参考脸相似度",
			"frame_processors_checkbox_group": "帧处理器",
			"face_debugger_items_checkbox_group": "脸部调试器选项",
			"face_enhancer_model_dropdown": "脸部增强模型",
			"face_enhancer_blend_slider": "脸部增强融合量",
			"face_swapper_model_dropdown": "脸部替换模型",
			"frame_enhancer_model_dropdown": "帧增强器模型",
			"frame_enhancer_blend_slider": "帧增强器融合量",
			"lip_syncer_model_dropdown": "嘴唇同步模型",
			"video_memory_strategy_dropdown": "视频存储策略",
			"system_memory_limit_slider": "系统内存限制",
			"output_image_or_video": "输出",
			"output_path_textbox": "输出路径",
			"output_image_quality_slider": "输出图像质量",
			"output_image_resolution_dropdown": "输出图像分辨率",
			"output_video_encoder_dropdown": "输出视频编码器",
			"output_video_preset_dropdown": "输出视频预设",
			"output_video_quality_slider": "输出视频质量",
			"output_video_resolution_dropdown": "输出视频分辨率",
			"output_video_fps_slider": "输出视频fps",
			"preview_image": "预览",
			"preview_frame_slider": "预览帧",
			"source_file": "源",
			"target_file": "目标",
			"temp_frame_format_dropdown": "临时帧图片格式",
			"trim_frame_start_slider": "裁剪帧开始位置",
			"trim_frame_end_slider": "裁剪帧结束位置",
			"webcam_image": "图像捕捉",
			"webcam_mode_radio": "图像捕捉模式",
			"webcam_resolution_dropdown": "图像捕捉分辨率",
			"webcam_fps_slider": "图像捕捉帧率"
		}
	}

WORDING_25: Dict[str, Any] = \
	{
		'conda_not_activated': 'Conda is not activated',
		'python_not_supported': 'Python version is not supported, upgrade to {version} or higher',
		'ffmpeg_not_installed': 'FFMpeg is not installed',
		'creating_temp': 'Creating temporary resources',
		'extracting_frames': 'Extracting frames with a resolution of {resolution} and {fps} frames per second',
		'extracting_frames_succeed': 'Extracting frames succeed',
		'extracting_frames_failed': 'Extracting frames failed',
		'analysing': 'Analysing',
		'processing': 'Processing',
		'downloading': 'Downloading',
		'temp_frames_not_found': 'Temporary frames not found',
		'copying_image': 'Copying image with a resolution of {resolution}',
		'copying_image_succeed': 'Copying image succeed',
		'copying_image_failed': 'Copying image failed',
		'finalizing_image': 'Finalizing image with a resolution of {resolution}',
		'finalizing_image_succeed': 'Finalizing image succeed',
		'finalizing_image_skipped': 'Finalizing image skipped',
		'merging_video': 'Merging video with a resolution of {resolution} and {fps} frames per second',
		'merging_video_succeed': 'Merging video succeed',
		'merging_video_failed': 'Merging video failed',
		'skipping_audio': 'Skipping audio',
		'restoring_audio_succeed': 'Restoring audio succeed',
		'restoring_audio_skipped': 'Restoring audio skipped',
		'clearing_temp': 'Clearing temporary resources',
		'processing_stopped': 'Processing stopped',
		'processing_image_succeed': 'Processing to image succeed in {seconds} seconds',
		'processing_image_failed': 'Processing to image failed',
		'processing_video_succeed': 'Processing to video succeed in {seconds} seconds',
		'processing_video_failed': 'Processing to video failed',
		'model_download_not_done': 'Download of the model is not done',
		'model_file_not_present': 'File of the model is not present',
		'select_image_source': 'Select a image for source path',
		'select_audio_source': 'Select a audio for source path',
		'select_video_target': 'Select a video for target path',
		'select_image_or_video_target': 'Select a image or video for target path',
		'select_file_or_directory_output': 'Select a file or directory for output path',
		'no_source_face_detected': 'No source face detected',
		'frame_processor_not_loaded': 'Frame processor {frame_processor} could not be loaded',
		'frame_processor_not_implemented': 'Frame processor {frame_processor} not implemented correctly',
		'ui_layout_not_loaded': 'UI layout {ui_layout} could not be loaded',
		'ui_layout_not_implemented': 'UI layout {ui_layout} not implemented correctly',
		'stream_not_loaded': 'Stream {stream_mode} could not be loaded',
		'point': '.',
		'comma': ',',
		'colon': ':',
		'question_mark': '?',
		'exclamation_mark': '!',
		'help':
			{
				# installer
				'install_dependency': 'select the variant of {dependency} to install',
				'skip_conda': 'skip the conda environment check',
				# general
				'source': 'choose single or multiple source images or audios',
				'target': 'choose single target image or video',
				'output': 'specify the output file or directory',
				# misc
				'force_download': 'force automate downloads and exit',
				'skip_download': 'omit automate downloads and remote lookups',
				'headless': 'run the program without a user interface',
				'log_level': 'adjust the message severity displayed in the terminal',
				# execution
				'execution_providers': 'accelerate the model inference using different providers (choices: {choices}, ...)',
				'execution_thread_count': 'specify the amount of parallel threads while processing',
				'execution_queue_count': 'specify the amount of frames each thread is processing',
				# memory
				'video_memory_strategy': 'balance fast frame processing and low VRAM usage',
				'system_memory_limit': 'limit the available RAM that can be used while processing',
				# face analyser
				'face_analyser_order': 'specify the order in which the face analyser detects faces',
				'face_analyser_age': 'filter the detected faces based on their age',
				'face_analyser_gender': 'filter the detected faces based on their gender',
				'face_detector_model': 'choose the model responsible for detecting the face',
				'face_detector_size': 'specify the size of the frame provided to the face detector',
				'face_detector_score': 'filter the detected faces base on the confidence score',
				'face_landmarker_score': 'filter the detected landmarks base on the confidence score',
				# face selector
				'face_selector_mode': 'use reference based tracking or simple matching',
				'reference_face_position': 'specify the position used to create the reference face',
				'reference_face_distance': 'specify the desired similarity between the reference face and target face',
				'reference_frame_number': 'specify the frame used to create the reference face',
				# face mask
				'face_mask_types': 'mix and match different face mask types (choices: {choices})',
				'face_mask_blur': 'specify the degree of blur applied the box mask',
				'face_mask_padding': 'apply top, right, bottom and left padding to the box mask',
				'face_mask_regions': 'choose the facial features used for the region mask (choices: {choices})',
				# frame extraction
				'trim_frame_start': 'specify the the start frame of the target video',
				'trim_frame_end': 'specify the the end frame of the target video',
				'temp_frame_format': 'specify the temporary resources format',
				'keep_temp': 'keep the temporary resources after processing',
				# output creation
				'output_image_quality': 'specify the image quality which translates to the compression factor',
				'output_image_resolution': 'specify the image output resolution based on the target image',
				'output_video_encoder': 'specify the encoder use for the video compression',
				'output_video_preset': 'balance fast video processing and video file size',
				'output_video_quality': 'specify the video quality which translates to the compression factor',
				'output_video_resolution': 'specify the video output resolution based on the target video',
				'output_video_fps': 'specify the video output fps based on the target video',
				'skip_audio': 'omit the audio from the target video',
				# frame processors
				'frame_processors': 'load a single or multiple frame processors. (choices: {choices}, ...)',
				'face_debugger_items': 'load a single or multiple frame processors (choices: {choices})',
				'face_enhancer_model': 'choose the model responsible for enhancing the face',
				'face_enhancer_blend': 'blend the enhanced into the previous face',
				'face_swapper_model': 'choose the model responsible for swapping the face',
				'frame_colorizer_model': 'choose the model responsible for colorizing the frame',
				'frame_colorizer_blend': 'blend the colorized into the previous frame',
				'frame_enhancer_model': 'choose the model responsible for enhancing the frame',
				'frame_enhancer_blend': 'blend the enhanced into the previous frame',
				'lip_syncer_model': 'choose the model responsible for syncing the lips',
				# uis
				'ui_layouts': 'launch a single or multiple UI layouts (choices: {choices}, ...)'
			},
		'uis':
			{
				# general
				'start_button': 'START',
				'stop_button': 'STOP',
				'clear_button': 'CLEAR',
				# about
				'donate_button': 'DONATE',
				# benchmark
				'benchmark_results_dataframe': 'BENCHMARK RESULTS',
				# benchmark options
				'benchmark_runs_checkbox_group': 'BENCHMARK RUNS',
				'benchmark_cycles_slider': 'BENCHMARK CYCLES',
				# common options
				'common_options_checkbox_group': 'OPTIONS',
				# execution
				'execution_providers_checkbox_group': 'EXECUTION PROVIDERS',
				# execution queue count
				'execution_queue_count_slider': 'EXECUTION QUEUE COUNT',
				# execution thread count
				'execution_thread_count_slider': 'EXECUTION THREAD COUNT',
				# face analyser
				'face_analyser_order_dropdown': 'FACE ANALYSER ORDER',
				'face_analyser_age_dropdown': 'FACE ANALYSER AGE',
				'face_analyser_gender_dropdown': 'FACE ANALYSER GENDER',
				'face_detector_model_dropdown': 'FACE DETECTOR MODEL',
				'face_detector_size_dropdown': 'FACE DETECTOR SIZE',
				'face_detector_score_slider': 'FACE DETECTOR SCORE',
				'face_landmarker_score_slider': 'FACE LANDMARKER SCORE',
				# face masker
				'face_mask_types_checkbox_group': 'FACE MASK TYPES',
				'face_mask_blur_slider': 'FACE MASK BLUR',
				'face_mask_padding_top_slider': 'FACE MASK PADDING TOP',
				'face_mask_padding_right_slider': 'FACE MASK PADDING RIGHT',
				'face_mask_padding_bottom_slider': 'FACE MASK PADDING BOTTOM',
				'face_mask_padding_left_slider': 'FACE MASK PADDING LEFT',
				'face_mask_region_checkbox_group': 'FACE MASK REGIONS',
				# face selector
				'face_selector_mode_dropdown': 'FACE SELECTOR MODE',
				'reference_face_gallery': 'REFERENCE FACE',
				'reference_face_distance_slider': 'REFERENCE FACE DISTANCE',
				# frame processors
				'frame_processors_checkbox_group': 'FRAME PROCESSORS',
				# frame processors options
				'face_debugger_items_checkbox_group': 'FACE DEBUGGER ITEMS',
				'face_enhancer_model_dropdown': 'FACE ENHANCER MODEL',
				'face_enhancer_blend_slider': 'FACE ENHANCER BLEND',
				'face_swapper_model_dropdown': 'FACE SWAPPER MODEL',
				'frame_colorizer_model_dropdown': 'FRAME COLORIZER MODEL',
				'frame_colorizer_blend_slider': 'FRAME COLORIZER BLEND',
				'frame_enhancer_model_dropdown': 'FRAME ENHANCER MODEL',
				'frame_enhancer_blend_slider': 'FRAME ENHANCER BLEND',
				'lip_syncer_model_dropdown': 'LIP SYNCER MODEL',
				# memory
				'video_memory_strategy_dropdown': 'VIDEO MEMORY STRATEGY',
				'system_memory_limit_slider': 'SYSTEM MEMORY LIMIT',
				# output
				'output_image_or_video': 'OUTPUT',
				# output options
				'output_path_textbox': 'OUTPUT PATH',
				'output_image_quality_slider': 'OUTPUT IMAGE QUALITY',
				'output_image_resolution_dropdown': 'OUTPUT IMAGE RESOLUTION',
				'output_video_encoder_dropdown': 'OUTPUT VIDEO ENCODER',
				'output_video_preset_dropdown': 'OUTPUT VIDEO PRESET',
				'output_video_quality_slider': 'OUTPUT VIDEO QUALITY',
				'output_video_resolution_dropdown': 'OUTPUT VIDEO RESOLUTION',
				'output_video_fps_slider': 'OUTPUT VIDEO FPS',
				# preview
				'preview_image': 'PREVIEW',
				'preview_frame_slider': 'PREVIEW FRAME',
				# source
				'source_file': 'SOURCE',
				# target
				'target_file': 'TARGET',
				# temp frame
				'temp_frame_format_dropdown': 'TEMP FRAME FORMAT',
				# trim frame
				'trim_frame_start_slider': 'TRIM FRAME START',
				'trim_frame_end_slider': 'TRIM FRAME END',
				# webcam
				'webcam_image': 'WEBCAM',
				# webcam options
				'webcam_mode_radio': 'WEBCAM MODE',
				'webcam_resolution_dropdown': 'WEBCAM RESOLUTION',
				'webcam_fps_slider': 'WEBCAM FPS'
			}
	}


def convert_wording(new_wording, old_chinese_wording):
	new_wording = new_wording.copy ()
	for k, v in new_wording.items ():
		if k in old_chinese_wording.keys ():
			wv = old_chinese_wording[k]
			if isinstance (v, dict) and isinstance (wv, dict):
				for k1, v1 in v.items ():
					if k1 in wv.keys ():
						new_wording[k][k1] = wv[k1]
					else:
						print ('no exit k={},k1={},v1={}'.format (k, k1, v1))
			elif isinstance (v, str):
				new_wording[k] = wv
			else:
				print ('no exit k={},v={}'.format (k, v))
		else:
			print ('no exit k={},v={}'.format (k, v))
	import json

	with open ('wording.json', 'w', encoding='utf-8') as w:
		json.dump (new_wording, w, ensure_ascii=False)


if __name__ == '__main__':
	# 新添加的可以自行翻译
	convert_wording(WORDING_25, CHINESE_WORDING_24)

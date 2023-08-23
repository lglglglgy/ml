#!/bin/bash

source_dir="/home/wqy/SNNs-RNNs/N_MNIST_DATA/"
target_dir="/home/lgy/ml/N-MNIST/data/"

# 创建目标目录，如果不存在
mkdir -p "$target_dir"

# 遍历源目录中的所有 .mat 文件
find "$source_dir" -type f -name "*.mat" | while read -r filepath; do
    # 提取文件名（不包括路径和后缀）
    filename=$(basename "$filepath" .mat)
    
    # 构建软链接目标路径
    link_path="$target_dir$filename.mat"
    
    # 创建软链接
    ln -s "$filepath" "$link_path"
    
    echo "Created symlink: $link_path"
done

echo "All .mat files have been linked to $target_dir"

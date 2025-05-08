# 40 Most Used Linux Commands for Artificial Intelligence

## System Management
1. **nvidia-smi** - Monitor NVIDIA GPU usage and memory
   ```bash
   nvidia-smi
   ```

2. **htop** - Interactive process viewer (CPU, memory usage)
   ```bash
   htop
   ```

3. **watch** - Execute a command periodically and display output
   ```bash
   watch -n 1 nvidia-smi
   ```

4. **tmux** - Terminal multiplexer for running multiple sessions
   ```bash
   tmux new -s ai_training
   ```

5. **screen** - Terminal multiplexer alternative
   ```bash
   screen -S training_session
   ```

## File Management

6. **rsync** - Synchronize files/directories efficiently
   ```bash
   rsync -avz --progress dataset/ remote_server:~/datasets/
   ```

7. **tar** - Archive files (commonly used for datasets)
   ```bash
   tar -czvf model_weights.tar.gz ./model/weights/
   ```

8. **scp** - Securely copy files between hosts
   ```bash
   scp large_model.h5 username@remote:/path/to/models/
   ```

9. **find** - Search for files in a directory hierarchy
   ```bash
   find . -name "*.py" -type f -exec grep "import tensorflow" {} \;
   ```

10. **du** - Estimate file space usage
    ```bash
    du -sh ./datasets/*
    ```

## Python & Environment Management

11. **pip** - Python package installer
    ```bash
    pip install tensorflow torch transformers
    ```

12. **conda** - Package and environment manager
    ```bash
    conda create -n nlp_env python=3.9 pytorch torchvision
    ```

13. **python** - Run Python scripts
    ```bash
    python train.py --epochs 100 --batch_size 32
    ```

14. **jupyter** - Start Jupyter notebook server
    ```bash
    jupyter notebook --ip=0.0.0.0 --port=8888
    ```

15. **virtualenv** - Create isolated Python environments
    ```bash
    virtualenv -p python3.9 ./venv
    ```

## Docker & Containers

16. **docker run** - Run a container
    ```bash
    docker run --gpus all -it tensorflow/tensorflow:latest-gpu
    ```

17. **docker build** - Build a Docker image
    ```bash
    docker build -t my_ai_app .
    ```

18. **docker-compose** - Define and run multi-container applications
    ```bash
    docker-compose up -d
    ```

19. **docker ps** - List running containers
    ```bash
    docker ps -a
    ```

20. **docker exec** - Execute a command in a running container
    ```bash
    docker exec -it tensorflow_container bash
    ```

## Data Processing

21. **awk** - Pattern scanning and processing language
    ```bash
    awk '{print $1,$3}' dataset.csv > extracted_columns.csv
    ```

22. **sed** - Stream editor for filtering and transforming text
    ```bash
    sed 's/old_label/new_label/g' annotations.txt > updated_annotations.txt
    ```

23. **grep** - Search text patterns
    ```bash
    grep -r "accuracy" ./logs/
    ```

24. **sort** - Sort lines of text files
    ```bash
    sort -n -k2 results.txt
    ```

25. **cut** - Remove sections from lines of files
    ```bash
    cut -d',' -f1,3 data.csv > subset.csv
    ```

## Network & API

26. **curl** - Transfer data from or to a server
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"text":"Analyze this"}' http://localhost:5000/predict
    ```

27. **wget** - Non-interactive network downloader
    ```bash
    wget https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-12_H-768_A-12.zip
    ```

28. **nc** (netcat) - Networking utility for reading/writing network connections
    ```bash
    nc -l 8080 > received_data.json
    ```

29. **ssh** - Secure shell client
    ```bash
    ssh -L 8888:localhost:8888 username@remote_gpu_server
    ```

30. **tensorboard** - TensorFlow's visualization toolkit
    ```bash
    tensorboard --logdir=./logs/
    ```

## Performance & Monitoring

31. **time** - Measure program execution time
    ```bash
    time python benchmark.py
    ```

32. **top** - Display Linux processes
    ```bash
    top
    ```

33. **iostat** - Report CPU and I/O statistics
    ```bash
    iostat -x 2
    ```

34. **free** - Display amount of free and used memory
    ```bash
    free -h
    ```

35. **ps** - Report process status
    ```bash
    ps aux | grep python
    ```

## Git & Version Control

36. **git clone** - Clone a repository
    ```bash
    git clone https://github.com/huggingface/transformers.git
    ```

37. **git pull** - Fetch from and integrate with another repository
    ```bash
    git pull origin main
    ```

38. **git commit** - Record changes to the repository
    ```bash
    git commit -m "Improved model accuracy by 2.5%"
    ```

39. **git push** - Update remote refs along with associated objects
    ```bash
    git push origin feature/new-model
    ```

40. **git lfs** - Git extension for versioning large files
    ```bash
    git lfs track "*.h5" "*.pkl" "*.bin"
    ```

## Bonus Commands

- **wandb** - Weight & Biases CLI for experiment tracking
  ```bash
  wandb init
  ```

- **ray** - Distributed computing framework
  ```bash
  ray start --head
  ```

- **mlflow** - Platform for ML lifecycle
  ```bash
  mlflow ui
  ```

- **dvc** - Data Version Control
  ```bash
  dvc add large_dataset/
  ```

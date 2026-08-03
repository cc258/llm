# uv + systemd 部署（最简版）

## 服务器初始化（只做一次）

```bash
# 1. 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. 克隆项目
cd /你的项目目录
git clone 你的仓库地址 llm && cd llm

# 3. 同步依赖
uv sync

# 4. 创建 .env
echo 'DASHSCOPE_API_KEY=你的Key' > .env

# 5. 创建 systemd 服务
sudo tee /etc/systemd/system/llm.service << 'EOF'
[Unit]
Description=LLM RAG Service
After=network.target

[Service]
Type=simple
WorkingDirectory=/你的项目目录/llm
ExecStart=/root/.local/bin/uv run streamlit run rag/qa.py --server.port 8501 --server.address 0.0.0.0
Restart=always
EnvironmentFile=/你的项目目录/llm/.env

[Install]
WantedBy=multi-user.target
EOF

# 6. 启动
sudo systemctl enable llm
sudo systemctl start llm

# 7. 配置 Caddy
# 在 Caddyfile 添加：
# your-domain.com {
#     reverse_proxy localhost:8501
# }
```

## GitHub Secrets

仓库 → Settings → Secrets → Actions：
```
SERVER_HOST = 服务器IP
SERVER_USER = 用户名
SERVER_PORT = 22
SSH_PRIVATE_KEY = SSH私钥
DEPLOY_PATH = /你的项目目录/llm
```

## 完成

推送代码后自动执行：
```bash
git pull
uv sync --frozen
sudo systemctl restart llm
```

## 常用命令

```bash
sudo systemctl status llm      # 查看状态
sudo systemctl restart llm     # 重启
sudo journalctl -u llm -f      # 实时日志
```

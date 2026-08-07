#!/bin/bash
# 服务器一键初始化脚本（首次部署时运行一次）
set -e

echo "=== LLM 项目服务器初始化 ==="

# 1. 安装 systemd 服务
echo "🔧 配置 systemd 服务..."
cp deploy/systemd/llm-qa.service /etc/systemd/system/
cp deploy/systemd/llm-agent.service /etc/systemd/system/

# 2. 重载并启用所有服务
systemctl daemon-reload
systemctl enable llm-qa llm-agent
systemctl start llm-qa llm-agent

# 3. 安装 Caddy（如果未安装）
if ! command -v caddy &> /dev/null; then
    echo "📦 安装 Caddy..."
    apt-get install -y debian-keyring debian-archive-keyring apt-transport-https curl
    curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
    curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list
    apt-get update
    apt-get install -y caddy
fi

# 4. 配置 Caddy
echo "🔧 配置 Caddy..."
cp deploy/Caddyfile /etc/caddy/Caddyfile
systemctl restart caddy

# 5. 验证
echo ""
echo "=== 验证服务状态 ==="
systemctl is-active llm-qa && echo "✅ QA 服务运行中" || echo "❌ QA 服务异常"
systemctl is-active llm-agent && echo "✅ Agent 服务运行中" || echo "❌ Agent 服务异常"
systemctl is-active caddy && echo "✅ Caddy 运行中" || echo "❌ Caddy 异常"

echo ""
echo "=== 完成！ ==="
echo "访问地址："
echo "  QA 页面:   http://你的域名/qa/"
echo "  Agent 页面: http://你的域名/agent/"

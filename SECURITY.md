# 安全说明

这个仓库是公开学习版，不应该包含任何真实业务凭据或真实商品资产。

## 不要提交的内容

- `.env`
- 真实 `API_KEY`
- 真实 `COOKIES_STR`
- 数据库文件
- 真实商品清单、货源链接、库存、售价、售后边界
- 支付码、群二维码、联系方式截图

## 公开版默认行为

- `ENABLE_LIVE_PLATFORM=false`
- 不自动索要 Cookie
- 不自动写回 `.env`
- 不附带真实联调资产

## 本地自测建议

1. 使用你自己的合法账号和配置
2. 把 `.env.example` 复制为 `.env`
3. 仅在本地把 `ENABLE_LIVE_PLATFORM` 改为 `true`
4. 推送前执行 `git status --ignored`

# 在 Fork 的仓库中启用 GitHub Pages（简单方法）

我发现 phenom-films/dayu_widgets 仓库使用了 GitHub Pages 的默认设置，这是一种非常简单但有效的方法。您可以按照以下步骤在您的仓库中实现相同的设置：

## 1. 确保文档在正确的位置

您的文档已经在正确的位置：主分支（master）的 `docs/` 目录下。

## 2. 启用 GitHub Pages

1. 打开您的 GitHub 仓库页面 (https://github.com/zhuoxyang/dayu_widgets3)
2. 点击 "Settings"（设置）
3. 在左侧菜单中找到 "Pages"
4. 在 "Build and deployment" 部分：
   - Source: 选择 "Deploy from a branch"
   - Branch: 选择 "master"（或您的默认分支）
   - 文件夹: 选择 "/docs"
5. 点击 "Save"（保存）

![GitHub Pages 设置示例](https://docs.github.com/assets/cb-28613/mw-1440/images/help/pages/publishing-source-drop-down.webp)

## 3. 等待部署完成

- 部署过程通常需要几分钟
- 部署完成后，您将在 Pages 设置页面看到一个绿色的成功消息和您的站点 URL
- 您的文档将可以通过以下 URL 访问：
  `https://zhuoxyang.github.io/dayu_widgets3/`

## 4. 验证文档是否正常工作

- 访问上述 URL
- 检查文档是否正确显示
- 检查链接是否正常工作
- 检查图片是否正常显示

## 为什么这种方法更简单？

1. **不需要复杂的工作流**：不需要创建和维护 GitHub Actions 工作流文件
2. **自动部署**：每次推送到主分支时，GitHub Pages 会自动更新
3. **更少的配置**：只需在仓库设置中进行一次简单的配置
4. **与原始仓库一致**：这与 phenom-films/dayu_widgets 使用的方法相同

## 常见问题

### 如果部署失败

1. 确保您的仓库设置中 GitHub Pages 的源设置正确（master 分支，/docs 文件夹）
2. 确保 `docs/` 目录中包含 `index.html` 文件
3. 等待几分钟，GitHub Pages 的部署可能需要一些时间

### 如果文档显示不正确

1. 检查 `docs/index.html` 中的资源路径是否正确指向您的仓库
2. 确保您的仓库中有所有必要的文档文件
3. 尝试在本地使用 `docsify serve docs` 预览文档，确保本地可以正常显示

如果您仍然遇到问题，请随时联系我寻求进一步的帮助。

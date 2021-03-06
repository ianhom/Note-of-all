# git
- git clone 克隆仓库
   - `git clone https://github.com/ianhom/moe.git`
- git status 检查状态，当前修改的文件，新增的文件和已经add但未commit的文件
- git add 增加修改记录
- git commit 在本地提交修改
- git push 提交到远端服务器
- git pull 将远端服务器同步到本地
- git branch 检查分支
- git checkout 切换分支，也可以用于撤销某个文件的修改
   - (branch) 切换某个分支
   - (commit id) 回退到某个commit
   - (file name) 撤销某个文件的修改
- git checkout -b 创建新分支并切换至新分支。
- git log 输出修改记录
- git shortlog 输出修改记录简要
- git merge 合并分支
- git reset 版本回退
- git diff 比较修改内容
- git config 配置git仓库
- git apply 应用patch
- git am 打patch并commit
- git init 初始化git仓库
- git submodule 子模块操作
   - add xxx.git yyy 增加xxx子模块到yyy路径下
   - status 检查子模块状态
   - sync 同步子模块信息
   - init 初始化子模块信息
   - update 下载更新子模块
- git show 显示已经commit后的修改内容
- git blame 显示文件的修改记录。
- git rm 删除文件在git中的管理。
- git rebase 将其他分支内容作为基础拉进当前分支。
- git rebase -i 修改commit记录。
   - drop 可删除commit。
   - reword 修改commit message
   - edit 修改commit
   - pick 选择该commit
- git fetch 同步远程分支。
- git clean 清除分支修改。
- git grep 搜索内容。
- git mv git管理内的移动。
- git cherry-pick 选择一个commit合入。
- git reflog git相关操作记录
- git stash 暂缓未commit的修改。
- git stash pop可将缓存数据恢复。
- git remote 检查远端信息。
- gitk 可视化管理。
- git format-patch 制作补丁文件
   - `git format-patch -1`

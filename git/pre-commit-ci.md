# [Pre-commit CI](https://pre-commit.ci/)

You use this as a "CI Service" which runs independently of Github Actions.
On the [home page](https://pre-commit.ci) you log in to github, give pre-commit-ci access,
and select which repos to operate on.
It then uses the `.pre-commit-config.yaml` file to run the pre-commit checks.
There is an optional `ci` key where you can specify non-default CI options.

When you push, it runs the pre-commit checks and you see an orange dot/green tick next the commit,
and if you click on that it takes you to the results page.

Here's a nice write-up I found after I'd already figured this out 🙄 https://blog.nshephard.dev/posts/pre-commit-ci/

If you push direct to master and the tests fail, nothing further happens.
If you're making a PR, then it will make any corrections that it can as a new commit on that branch.
If it isn't obvious how to fix the problem, that error remains as an outstanding failed test.

It looks like these checks run on every branch on every push.
This seems rather wasteful, but I can't see a way to specify only to run on PRs, master, etc.
So I've asked the question: pre-commit-ci/issues#263

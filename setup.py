from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='project-hitman',
    version='1.0.0',
    description='Project HITMAN: AI-Powered Task Resolution System',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='US Department of Special Projects and Unified Response Services',
    author_email='admin@spurs.agency',
    url='https://github.com/usdos/hitman',
    packages=find_packages(),
    install_requires=[
        'anthropic==0.2.2',
        'openai==0.27.0',
        'google-cloud-aiplatform==1.21.0',
        'cloudflare==2.11.0',
        'requests==2.32.0',
        'pyyaml==6.0',
        'python-dotenv==0.21.0',
        'google-api-python-client==2.70.0',
        'google-auth-oauthlib==0.5.3',
        'google-auth-httplib2==0.1.0',
        'microsoft-graph==1.0.0',
        'celery==5.2.7',
        'redis==4.4.4',
        'flower==1.2.0',
    ],
    extras_require={
        'dev': [
            'pytest==7.1.2',
            'black==24.3.0',
            'flake8==4.0.1',
            'pre-commit==2.20.0',
            'sphinx==4.5.0',
            'sphinx-rtd-theme==1.0.0',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
)
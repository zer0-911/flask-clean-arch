<!-- git remote add origin https|ssh:path/to/the/repository.git  -->
<!-- git pull origin main --rebase -->
<div align="center">
<h1> Flask Clean Architecture </h1>
<a href="https://github.com/zer0-911/flask-clean-arch/header.png">
    <img src="./img/header.png" alt="flask-clean-arch">
</a>

<!-- You can make badge by read on official documentation at https://shields.io/badges -->

</div>
<p align="center">
<a target="_blank" href="https://www.linkedin.com/in/moh-iqbal-fatchurozi/"><img height="20" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a target="_blank" href=""><img height="20" src="https://img.shields.io/github/license/zer0-911/flask-clean-arch" alt="License"></a>
<a target="_blank" href=""><img height="20" src="https://img.shields.io/github/commit-activity/t/zer0-911/flask-clean-arch" alt="Last Commits"></a>
<a target="_blank" href=""><img height="20" src="https://img.shields.io/github/repo-size/zer0-911/flask-clean-arch" alt="Repo Size"></a>
</p>

<p align="center">
<a href="#-introduction">Introduction</a> &nbsp;&bull;&nbsp;
<a href="#-tech-stack">Tech Stack</a> &nbsp;&bull;&nbsp;
<a href="#%EF%B8%8F-installation">Installation</a> &nbsp;&bull;&nbsp;
<a href="#-reference">Reference</a>&nbsp;&bull;&nbsp;
<a href="#-issue">Issue</a>&nbsp;&bull;&nbsp;
<a href="#-license">License</a>&nbsp;&bull;&nbsp;
<a href="#-author">Author</a>
</p>

## 📄 Introduction

`Flask Clean Architecture` is a project template designed to help developers build scalable and maintainable web applications using the Flask framework. It follows the principles of Clean Architecture, ensuring a clear separation of concerns and promoting best practices in software development. This template provides a solid foundation for your Flask projects, including a well-structured directory layout, essential configurations, and integration with popular tools and libraries.

## 💻 Tech Stack

> Framework, Library, Database, Tools, etc

<!-- You can search the logo with https://simpleicons.org and copy the name in logo=copyhere same with color after badge/YourText-YourColor-->

- <a target="_blank" href="https://www.postgresql.org/">
      <img height="20" src="https://img.shields.io/badge/Postgresql-0D96F6?style=for-the-badge&logo=postgresql&logoColor=white" alt="postgresql"/>
  </a>
- etc

## ⚙️ Installation

1. Clone this repository `git clone https://github.com/zer0-911/flask-clean-arch or click `Clone or Download`button and then click`Download ZIP`
   > Optional: Recommended to use virtual environment
2. Copy the `.env.example` file to `.env` and update the environment variables
   ```bash
   cp .env.example .env
   ```
3. Install dependencies by running
   ```bash
   pip install -r requirements.txt
   ```
4. Create the database and run the migrations
   ```bash
   flask db upgrade
   ```
5. Run the app

   ```bash
   flask run -h 0.0.0.0 -p 3000
   ```

<!-- ## 📽️ Demo -->

<!-- If Needed  -->
<!-- <div align="center">
    <img src="./img/demo.gif" alt="Demo">
</div> -->

## 📚 Reference

<!-- If Needed -->

- [Understanding Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)

## 🚩 Issue

If you found a bug or an issue, please report by opening a new issue on [this repository](https://github.com/zer0-911/flask-clean-arch/issues).

## 📝 License

This project is licensed under the **MIT** License - see the [LICENSE](LICENSE) file for details

## 📌 Authors

<p align="center">
<h3> Moh. Iqbal Fatchurozi </h3>
<a target="_blank" href="https://www.linkedin.com/in/moh-iqbal-fatchurozi/"><img height="20" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="linkedin" /></a>
<a target="_blank" href="https://github.com/zer0-911"><img height="20" src="https://img.shields.io/badge/Github-000000?style=for-the-badge&logo=github&logoColor=white" alt="github"/></a>
<a target="_blank" href="https://iqbalfatchurozi.tech">
<img height="20" src="https://img.shields.io/badge/Portfolio-00BC8E?style=for-the-badge&logo=googlecloud&logoColor=white" alt="portofolio"/>
</a>
</p>

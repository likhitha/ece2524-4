#include "mymainwindow.h"
#include "ui_mymainwindow.h"
#include <QProcess>
#include <QByteArray>
#include <iostream>
#include <QDir>
#include <QColor>

using namespace std;

QProcess *hubProcess;

myMainWindow::myMainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::myMainWindow)
{
    ui->setupUi(this);

    // connect show scores button
    connect(ui->btnGetScores,SIGNAL(released()), this, SLOT(fetchScores()));
    connect(ui->btnAddScore, SIGNAL(released()), this, SLOT(addScore()));
    connect(ui->btnDelete, SIGNAL(released()), this, SLOT(deleteItem()));

    // set up seperate process outputs
    hubProcess = new QProcess(this);
    connect(hubProcess, SIGNAL(readyReadStandardOutput()), this, SLOT(outputData()));
    connect(hubProcess, SIGNAL(readyReadStandardError()), this, SLOT(errorData()));

}

myMainWindow::~myMainWindow()
{
    delete ui;
}

void myMainWindow::fetchScores() {
    ui->teScoreOutput->clear();
    if(ui->teGame->toPlainText().isEmpty()) ui->teScoreOutput->append("Game name needed.");
    else {
        cout << "running process" << endl;
        ui->teScoreOutput->append("<u>User&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Score</u>");
        QString exe = "/usr/bin/python";
        QStringList args;
        args << QString(QDir::currentPath()+"/Hub.py") << "--list" << ui->teGame->toPlainText() << ui->teNumberOfScores->toPlainText();
        hubProcess->start(exe, args);
        hubProcess->waitForFinished();
    }
}

void myMainWindow::addScore() {
    ui->teScoreOutput->clear(); // clear the output area
    if(ui->teGame->toPlainText().isEmpty() || ui->teScore->toPlainText().isEmpty() || ui->teUser->toPlainText().isEmpty()) ui->teScoreOutput->append("Game name, User name, and score needed.");
    else {
        cout << "adding score..." << endl;
        QString exe = "/usr/bin/python";
        QStringList args;
        args << QString(QDir::currentPath()+"/Hub.py") << "--add" << ui->teGame->toPlainText() << ui->teUser->toPlainText() << ui->teScore->toPlainText();
        hubProcess->start(exe, args);
        hubProcess->waitForFinished();
        ui->teScoreOutput->append(ui->teUser->toPlainText() + "'s score of " + ui->teScore->toPlainText() + " was added to " + ui->teGame->toPlainText() + " data.");
    }
}

void myMainWindow::deleteItem() {
    cout << "removing score..." << endl;
    ui->teScoreOutput->clear();
    if(ui->teGame->toPlainText().isEmpty()) ui->teScoreOutput->append("Game name needed. User name optional.");
    else {
        QString exe = "/usr/bin/python";
        QStringList args;
        if(ui->teUser->toPlainText().isEmpty()) args << QString(QDir::currentPath()+"/Hub.py") << "--del" << ui->teGame->toPlainText();
        else args << QString(QDir::currentPath()+"/Hub.py") << "--del" << ui->teGame->toPlainText() << ui->teUser->toPlainText();
        hubProcess->start(exe, args);
        hubProcess->waitForFinished();
        if(ui->teUser->toPlainText().isEmpty()) ui->teScoreOutput->append(ui->teGame->toPlainText() + " data was deleted.");
        else ui->teScoreOutput->append(ui->teUser->toPlainText() + "'s score was deleted from " + ui->teGame->toPlainText() + " data.");
    }
}

void myMainWindow::outputData() {
    QByteArray processResult = hubProcess->readAllStandardOutput();
    QStringList strLines = QString(processResult).split('\n');

    foreach(QString line, strLines) {
        ui->teScoreOutput->append(line);
        ui->teScoreOutput->moveCursor( QTextCursor::End, QTextCursor::MoveAnchor );
        ui->teScoreOutput->moveCursor( QTextCursor::Left, QTextCursor::KeepAnchor );
        ui->teScoreOutput->textCursor().removeSelectedText();
    }
}

void myMainWindow::errorData() {
    cout << "Errors occured." << endl;
}

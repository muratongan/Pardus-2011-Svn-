#include "helper.h"
#include <iostream>
#include <QStringList>
#include <QFile>
#include <QTextStream>
#include <QDebug>

ActionReply Helper::createReply(int code, const QVariantMap *returnData)
{
    ActionReply reply;

    if (code) {
        reply = ActionReply::HelperError;
        reply.setErrorCode(code);
    } else {
        reply = ActionReply::SuccessReply;
    }

    if (returnData)
        reply.setData(*returnData);

    return reply;
}


bool Helper::writeKeyboard(const QString &layouts, const QString &variants)
{
    QString xorgFile = "/etc/X11/xorg.conf.d/00-configured-keymap.conf";

    QString xorgContent;
    xorgContent =   "# This file is generated by KCM Keyboard Module.\n"
                    "# If you want to change settings in this file, edit\n"
                    "# the file 10-keyboard.conf in the same directory.\n\n"
                    "Section \"InputClass\"\n"
                    "       Identifier\t\"Configured Keymap\"\n"
                    "       MatchisKeyboard\t\"on\"\n"
                    "       MatchTag\t\"use_configured_keymap\"\n\n"
                    "       Option\t\"xkb_layout\"\t\"" + layouts + "\"\n"
                    "       Option\t\"xkb_variant\"\t\"" + variants + "\"\n"
                    "EndSection\n";

    // open file to write
    QFile file(xorgFile);
    if( !file.open( QIODevice::WriteOnly | QIODevice::Text)) {
        qDebug() << "Failed to write.";
        return false;
    }

    // content of fields is saved to the new file
    QTextStream out(&file);
    out << xorgContent;
    file.close();

    return true;
}

ActionReply Helper::managekeyboard(QVariantMap args)
{
    int code = 0;

    QString layouts = args.value("layouts").toString();
    QString variants = args.value("variants").toString();

    code = (writeKeyboard(layouts,variants) ? 0 : WriteKeyboardError);
    return createReply(code);
}



KDE4_AUTH_HELPER_MAIN("org.kde.kcontrol.kcmkeyboard", Helper)

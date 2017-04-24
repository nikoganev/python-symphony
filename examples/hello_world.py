#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    hello world for symphony
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2017, Symphony'

import symphony


def main():
    ''' main program loop '''
    conn = symphony.Config('/etc/es-bot/es-bot.cfg')
    # connect to pod
    agent, pod, symphony_sid = conn.connect()
    # main loop
    msgFormat = 'MESSAGEML'
    message = '<messageML> hello world. </messageML>'
    # send message
    retstring = agent.send_message(symphony_sid, msgFormat, message)
    print(retstring)


if __name__ == "__main__":
    main()
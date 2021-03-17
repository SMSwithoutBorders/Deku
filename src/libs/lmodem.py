#!/bin/python

import subprocess
from subprocess import Popen, PIPE
from libs.lsms import SMS 
from messagestore import MessageStore as ms

import logging
import threading

class Modem():
    def __init__( self, index ):
        self.mmcli_m = ["mmcli", f"-Km", index]

        # Modem parse keys
        self.imei = "modem.3gpp.imei"
        self.sim = "modem.generic.sim"
        self.state = "modem.generic.state"
        self.device = "modem.generic.device"
        self.operator_name = "modem.3gpp.operator-name"
        self.operator_code = "modem.3gpp.operator-code"
        self.primary_port = "modem.generic.primary-port"
        self.device_identifier = "modem.generic.device-identifier"
        self.state_failed_reason = "modem.generic.state-failed-reason"
        self.equipment_identifier = "modem.generic.equipment-identifier"
        self.signal_quality_value = "modem.generic.signal-quality.value"
        self.access_technologies_values = "modem.generic.access-technologies.value[1]"


    def __bindObject( self, keys :list, value, _object=None):
        if _object == None:
            _object = {}

        if len(keys) > 1:
            if not keys[0] in _object:
                _object[keys[0]] = {}
            new_object = self.__bindObject(keys[1:], value, _object[keys[0]])
            # print(f"{len(keys)}: {new_object}")
            _object[keys[0]] = new_object
        else:
            _object = {keys[0] : value}
        return _object

    def __appendObject( self, kObject, tObject ):
        try:
            if type(tObject) == type(""):
                return {}
            if list(tObject.keys())[0] in kObject:
                key = list(tObject.keys())[0]
                new_object = self.__appendObject( kObject[key], tObject[key] )
                # print( new_object )
                if not new_object == {}:
                    kObject.update(new_object)
            else:
                kObject.update(tObject)
        except Exception as error:
            print(f"errtObject: ", tObject, type(tObject))
            print(error, "\n")

        return kObject


    @classmethod
    def extractInfo(cls, mmcli_output=None):
        try: 
            if mmcli_output == None:
                if hasattr(self, 'mmcli_m' ):
                    mmcli_output = subprocess.check_output(self.mmcli_m, stderr=subprocess.STDOUT).decode('utf-8')
                else:
                    raise Exception(f">> no input available to extract information")
        except subprocess.CalledProcessError as error:
            raise Exception(f"[stderr]>> return code[{error.returncode}], output[{error.output.decode('utf-8')}")
        else:
            # print(f"mmcli_output: {mmcli_output}")
            mmcli_output = mmcli_output.split('\n')
            m_details = {}
            for output in mmcli_output:
                m_detail = output.split(': ')
                if len(m_detail) < 2:
                    continue
                key = m_detail[0].replace(' ', '')
                m_details[key] = m_detail[1]

                indie_keys = key.split('.')
                # tmp_details = self.__bindObject( keys=indie_keys, value=m_detail[1] )
                tmp_details = __bindObject( keys=indie_keys, value=m_detail[1] )
                print("tmp_details>> ", tmp_details)
                m_details = __appendObject(m_details, tmp_details)
                # print("m_details>> ", m_details)
                # m_details.update( tmp_details )
            # print("m_details:", m_details)
            return m_details

    def readyState(self):
        m_details = self.info()
        if m_details[self.operator_code].isdigit() and m_details[self.signal_quality_value].isdigit() and m_details[self.sim] != '--':
            return True
        return False

    
    def __create(self, sms :SMS):
        mmcli_create_sms = []
        mmcli_create_sms += self.mmcli_m + sms.mmcli_create_sms
        mmcli_create_sms[-1] += '=number=' + sms.number + ",text='" + sms.text + "'"
        try: 
            mmcli_output = subprocess.check_output(mmcli_create_sms, stderr=subprocess.STDOUT).decode('utf-8').replace('\n', '')

        except subprocess.CalledProcessError as error:
            print(f"[stderr]>> return code[{error.returncode}], output[{error.output.decode('utf-8')}")
        else:
            print(f"{mmcli_output}")
            mmcli_output = mmcli_output.split(': ')
            creation_status = mmcli_output[0]
            sms_index = mmcli_output[1].split('/')[-1]
            if not sms_index.isdigit():
                print(f">> sms index isn't an index: {sms_index}")
            else:
                sms.index = sms_index
                # self.__send(sms)
        return sms

    def __send(self, sms: SMS):
        mmcli_send = self.mmcli_m + ["-s", sms.index, "--send"]
        try: 
            mmcli_output = subprocess.check_output(mmcli_send, stderr=subprocess.STDOUT).decode('utf-8').replace('\n', '')

        except subprocess.CalledProcessError as error:
            returncode = error.returncode
            err_output = error.output.decode('utf-8').replace('\n', '')
            print(f">> failed to send sms")
            print(f"\treturn code: {returncode}")
            print(f"\tstderr: {err_output}")
            # raise Exception( error )
        else:
            print(f"{mmcli_output}")
            return True

    def set_sms(self, sms :SMS):
        self.sms = self.__create( sms )
        return self.sms

    def send_sms(self, sms :SMS):
        return self.__send( sms )

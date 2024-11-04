from PT104 import PT104, Channels, DataTypes, Wires, CommunicationType
unit = PT104()
name=unit.discover_devices(communication_type=CommunicationType.CT_ETHERNET)
print(name)
exit(0)
name=name.split(b':')[-1]
unit.connect(name)
unit.connect(
        serial='AW733/077',
        interface=CommunicationType.CT_ETHERNET,
        address='192.168.0.69:11111'
)
if not unit.is_connected:
    exit(0)
unit.set_mains(sixty_hertz=False)
unit.set_channel(Channels.CHANNEL_1, DataTypes.PT100, Wires.WIRES_3, low_pass_filter=True)
unit.set_channel(Channels.CHANNEL_2, DataTypes.PT100, Wires.WIRES_3, low_pass_filter=True)
value1 = unit.get_value_channel_1
value2 = unit.get_value_channel_2
print(f'CH1: {value1}')
print(f'CH2: {value2}')
unit.disconnect()

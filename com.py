import click
import sys
import serial
import serial.tools.list_ports

VERSION = '0.0.0'

@click.group()
def cli():
    pass


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

@click.command()
def version():
    """获取版本号"""
    click.echo(VERSION)

@click.command()
@click.option('--vid', help='输入要查找的vid的16进制, 如: --vid=0x1234')
@click.option('--pid', help='输入要查找的pid的16进制, 如: --pid=0x4321')
def find(vid:str, pid:str):
    '''通过指定 vid pid号 查找com口名称'''
    port_list = list(serial.tools.list_ports.comports())
    vid_int = int(vid, 16)
    pid_int = int(pid, 16)
    for port in port_list:
        if port.pid != None and port.vid != None:
            click.echo(f'pid:{pid} vid:{vid} com:{port.name}')
            if port.vid == vid_int and port.pid == pid_int:
                click.echo(f'find com: {port.name}')
                sys.exit(0)

    click.secho('com not find', err=True, fg='red')
    sys.exit(1)

cli.add_command(hello)
cli.add_command(version)
cli.add_command(find)
if __name__ == '__main__':
    cli()
    sys.exit(0)
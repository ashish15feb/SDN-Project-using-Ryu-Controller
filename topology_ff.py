from mininet.topo import Topo
from mininet.link import TCLink


class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host11 = self.addHost( 'h11', ip='192.168.1.1/24' )
        host12 = self.addHost( 'h12', ip='192.168.1.1/24'  )
        host13 = self.addHost( 'h13', ip='192.168.1.1/24'  )

        host21 = self.addHost( 'h21', ip='192.168.1.11/24'  )
       # host22 = self.addHost( 'h22', ip='192.168.1.12/24'  )
       # host23 = self.addHost( 'h23', ip='192.168.1.13/24'  )

        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )

        #props1 = {'bw': 10, 'delay': '0ms'}
       # props2 = {'bw': 10, 'delay':'0ms'}
        #props3 = {'bw': 10, 'delay': '0ms'}

        # Add links
        self.addLink( host11, switch1)
        self.addLink( host12, switch1)
        self.addLink( host13, switch1)

        self.addLink( host21, switch2)
        #self.addLink( host22, switch2)
        #self.addLink( host23, switch2)


        self.addLink( switch1, switch2)
        #self.addLink( switch1, switch2, cls=TCLink, **props2)
        #self.addLink(switch1, switch2, cls=TCLink, **props3)
        
topos = { 'mytopo': ( lambda: MyTopo() ) }

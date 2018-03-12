from mininet.topo import Topo
from mininet.link import TCLink


class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host21 = self.addHost( 'h21', ip='10.10.2.1')
        host22 = self.addHost( 'h22', ip='10.10.2.2' )
        host31 = self.addHost( 'h31', ip='10.10.3.1' )
        host32 = self.addHost( 'h32', ip='10.10.3.2' )
        host41 = self.addHost( 'h41', ip='10.10.4.1' )
        host42 = self.addHost( 'h42', ip='10.10.4.2' )
        server80 = self.addHost( 'server80', ip='10.10.1.100' )
        server88 = self.addHost( 'server88', ip='10.10.1.200' )



        switch1 = self.addSwitch( 's1', mac='00:00:00:00:00:01' )
        switch2 = self.addSwitch( 's2', mac='00:00:00:00:00:02' )
        switch3 = self.addSwitch( 's3', mac='00:00:00:00:00:03' )
        switch4 = self.addSwitch( 's4', mac='00:00:00:00:00:04' )




        # Add links
        self.addLink( host21, switch2)
        self.addLink( host22, switch2)
        self.addLink( host31, switch3)
        self.addLink( host32, switch3)
        self.addLink( host41, switch4)
        self.addLink( host42, switch4)
        self.addLink( server80, switch1)
        self.addLink( server88, switch1)



        self.addLink( switch1, switch2)
        self.addLink( switch1, switch3)
        self.addLink( switch1, switch4)


        
topos = { 'mytopo': ( lambda: MyTopo() ) }


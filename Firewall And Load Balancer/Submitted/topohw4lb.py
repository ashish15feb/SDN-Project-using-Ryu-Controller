from mininet.topo import Topo
from mininet.link import TCLink


class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1', ip='10.10.1.1')
        host2 = self.addHost( 'h2', ip='10.10.1.2' )
        #host31 = self.addHost( 'h31', ip='10.10.3.1' )
        #host32 = self.addHost( 'h32', ip='10.10.3.2' )
        #host41 = self.addHost( 'h41', ip='10.10.4.1' )
        #host42 = self.addHost( 'h42', ip='10.10.4.2' )
        server1 = self.addHost( 'server1', ip='10.10.1.100' )
        server2 = self.addHost( 'server2', ip='10.10.1.150' )
        server3 = self.addHost('server3', ip='10.10.1.200')


        switch1 = self.addSwitch( 's1', mac='00:00:00:00:00:01' )
        #switch2 = self.addSwitch( 's2', mac='00:00:00:00:00:02' )
        #switch3 = self.addSwitch( 's3', mac='00:00:00:00:00:03' )
        #switch4 = self.addSwitch( 's4', mac='00:00:00:00:00:04' )




        # Add links
        self.addLink( host1, switch1)
        self.addLink( host2, switch1)
        #self.addLink( host31, switch3)
        #self.addLink( host32, switch3)
        #self.addLink( host41, switch4)
        #self.addLink( host42, switch4)
        self.addLink( server1, switch1)
        self.addLink( server2, switch1)
        self.addLink( server3, switch1)



        #self.addLink( switch1, switch2)
        #self.addLink( switch1, switch3)
        #self.addLink( switch1, switch4)


        
topos = { 'mytopo': ( lambda: MyTopo() ) }


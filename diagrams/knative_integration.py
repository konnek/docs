from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.oci.compute import Container
from diagrams.oci.monitoring import Queuing
from diagrams.oci.network import Routetable

with Diagram("Knative Integration", show=False):
    with Cluster("AWS"):
        konnek = Lambda("konnek")

    with Cluster("K8S"):
        receiver = Container("receiver")
        sinkbinding = Container("sinkbinding")
        broker = Queuing("broker")
        trigger = Routetable("trigger")
        consumer = Container("consumer")


    konnek >> receiver >> sinkbinding >> broker >> trigger >> consumer

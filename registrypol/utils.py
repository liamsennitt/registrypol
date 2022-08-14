from registrypol.policy import RegistryPolicy


def dump(policy, stream):
    stream.write(policy.to_bytes())


def load(stream):
    return RegistryPolicy.from_bytes(stream.read())

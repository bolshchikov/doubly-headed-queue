#!/usr/bin/python

import defs


def main ():
	'''Here starts the part written in main.cpp file'''

	dq1 = defs.DBL_Queue()
	dq1.enqueueBeg(4)
	dq1.enqueueBeg(7)
	dq1.enqueueEnd(17)
	dq1.enqueueEnd(567)
	dq1.enqueueBeg(324)
	dq1.dequeueEnd()
	dq1.enqueueEnd(789)
	dq1.dequeueBeg()
	dq1.printQueue()
	print ' queue size: %d \n' % dq1.get_queue_size()

	dq2 = defs.DBL_Queue()
	dq2.enqueueEnd(3)
	dq2.enqueueEnd(8)
	dq2.enqueueBeg(19)
	dq2.dequeueBeg()
	dq2.enqueueEnd(567)
	dq2.enqueueBeg(864)
	dq2.dequeueEnd()
	dq2.enqueueBeg(223)
	dq2.enqueueEnd(221)
	dq2.dequeueBeg()
	dq2.printQueue()
	print ' queue size: %d \n' % dq2.get_queue_size()

	dq1.concatQueue(dq2)
	dq1.printQueue()
	print ' queue size: %d \n' % dq1.get_queue_size()
	
	dq1.enqueueBeg(1)
	dq1.enqueueEnd(2)
	dq1.dequeueEnd()
	dq1.dequeueEnd()
	dq1.dequeueBeg()
	dq1.printQueue()
	print ' queue size: %d \n' % dq1.get_queue_size()

if __name__ == '__main__':
	main()